from typing import Dict, Any

from pydantic import BaseModel


class SlackEvent(BaseModel):
    event: Dict[str, Any]
