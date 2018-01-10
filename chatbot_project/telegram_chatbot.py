from telepot import Bot, glance
from telepot.loop import MessageLoop
from time import sleep
import pprint


################################################################################
class MyPrettyPrinter(pprint.PrettyPrinter):
	def format(self, _object, context, maxlevels, level):
		if isinstance(_object, unicode):
			return "'%s'" % _object.encode('utf8'), True, False
		elif isinstance(_object, str):
			_object = unicode(_object,'utf8')
			return "'%s'" % _object.encode('utf8'), True, False
		return pprint.PrettyPrinter.format(self, _object, context,maxlevels, level)
################################################################################
def my_pprint(d):
	MyPrettyPrinter().pprint(d)

################################################################################
def handle(msg):
	my_pprint(msg)
	content_type, chat_type, chat_id = glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		bot.sendMessage(chat_id, 'Re: %s' % msg['text'])
################################################################################
bot = Bot('534463139:AAHIFdVQoaQadKXaaK2w_q5wr-QilviTddE')
me = bot.getMe()
my_pprint(me)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
# Keep the program running.
while True:
	sleep(10)
