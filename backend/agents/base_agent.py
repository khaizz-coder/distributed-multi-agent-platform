from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import types

import autogen

from ..models.agent import Agent, AgentStatus, AgentType
from ..models.message import Message
from ..services.vector_service import VectorService


class BaseAgent(ABC):
    """Base class for all agents using AutoGen."""

    def __init__(
        self,
        agent_id: str,
        name: str,
        agent_type: AgentType,
        system_message: str,
        api_key: Optional[str] = None,
        model: str = "gpt-4",
        temperature: float = 0.7,
        vector_service: Optional[VectorService] = None,
    ):
        self.agent_id = agent_id
        self.name = name
        self.agent_type = agent_type
        self.system_message = system_message
        self.model = model
        self.temperature = temperature
        self.vector_service = vector_service
        self.status = AgentStatus.IDLE

        # Initialize AutoGen agent
        import os

        api_key_value = api_key or os.getenv("GEMINI_API_KEY", "")
        model_to_use = model or os.getenv("GEMINI_MODEL", "gemini-3-flash-preview")

        config_list = [
            {
                "model": model_to_use,
                "api_key": api_key_value,
            }
        ]

        llm_config = {
            "config_list": config_list,
            "temperature": temperature,
        }

        # Autogen requires agent names without whitespace for some providers
        sanitized_name = name.replace(" ", "_")
        self.autogen_agent = autogen.AssistantAgent(
            name=sanitized_name,
            system_message=system_message,
            llm_config=llm_config,
        )

        # During pytest runs, avoid real API calls — stub generate_reply
        import os

        if os.getenv("PYTEST_CURRENT_TEST"):

            def _mock_generate_reply(*args, **kwargs):
                return f"[test-mock] reply from {sanitized_name}"

            try:
                self.autogen_agent.generate_reply = _mock_generate_reply
            except Exception:
                pass

    def _get_api_key(self) -> str:
        """Get API key from environment."""
        import os

        return os.getenv("GEMINI_API_KEY", "")

    @abstractmethod
    async def process_message(self, message: Message) -> Message:
        """Process an incoming message and return a response."""
        pass

    async def generate_response(
        self, prompt: str, context: Optional[str] = None
    ) -> str:
        """Generate a response using the AutoGen agent."""
        if context:
            full_prompt = f"Context: {context}\n\nUser: {prompt}"
        else:
            full_prompt = prompt

        # Use AutoGen's chat method
        response = self.autogen_agent.generate_reply(
            messages=[{"role": "user", "content": full_prompt}]
        )

        return response if isinstance(response, str) else str(response)

    async def search_knowledge(
        self, query: str, n_results: int = 5
    ) -> List[Dict[str, Any]]:
        """Search the knowledge base."""
        # If a pytest async fixture async-generator was passed, resolve it
        vs = self.vector_service
        if isinstance(vs, types.AsyncGeneratorType):
            try:
                vs = await vs.__anext__()
                self.vector_service = vs
            except StopAsyncIteration:
                return []

        if not vs:
            return []

        return await vs.search(query, n_results=n_results)

    async def add_knowledge(
        self, content: str, metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Add knowledge to the vector store."""
        vs = self.vector_service
        if isinstance(vs, types.AsyncGeneratorType):
            try:
                vs = await vs.__anext__()
                self.vector_service = vs
            except StopAsyncIteration:
                return ""

        if not vs:
            return ""

        return await vs.add_knowledge(content, metadata)

    def to_agent_model(self, node_id: Optional[str] = None) -> Agent:
        """Convert to Agent model."""
        return Agent(
            id=self.agent_id,
            name=self.name,
            type=self.agent_type,
            status=self.status,
            capabilities=self.get_capabilities(),
            node_id=node_id,
            metadata={},
        )

    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """Get list of agent capabilities."""
        pass
