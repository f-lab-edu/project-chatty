from fastapi import APIRouter, Depends
from fastapi.logger import logger
from slack_sdk import WebClient

from schemas.slack_event import SlackEvent
from schemas.chat_response import ChatResponse
from service.slack_client import get_slack_client
from service.chat_service import DialogEngine
from utils.match_pattern import get_text

router = APIRouter()


@router.post("/slack")
async def get_slack_message(
    slack_event: SlackEvent,
    slack_client: WebClient = Depends(get_slack_client),
    chat_service: DialogEngine = Depends(),
) -> ChatResponse:
    slack_event = slack_event.event
    if "challenge" in slack_event:
        return {"challenge": slack_event["challenge"]}
    logger.warn(slack_event)

    received_text = get_text(full_text=slack_event["text"])
    channel = slack_event["channel"]
    client_id = slack_event["user"]

    response = f"<@{client_id}> {received_text}"
    slack_client.post_message(channel=channel, text=response)
    return {"msg": received_text}
