import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from inf import tok, botid
vk_session = vk_api.VkApi(token=tok)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, botid)
def send(text,attach=0):
    vk.messages.send(
        peer_id=event.obj.peer_id,
        random_id=get_random_id(),
        message=text,
        attachment=attach
    )

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        text=event.obj.text
        if text.lower().startswith(".kick "):
            mes=text.split()[1]
            mes=mes[mes.find("[")+1:mes.find("|")]
            id=vk.users.get(user_ids=mes)[0]['id']
            vk.messages.removeChatUser(chat_id=event.chat_id, user_id=id)