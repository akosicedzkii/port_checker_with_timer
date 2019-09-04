import time
import sys
import send_email
import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        send_email.send_message(message)

conn = stomp.Connection()
conn.set_listener('', MyListener())
conn.start()
conn.connect('user', 'user', wait=True)

conn.subscribe(destination='/queue/test', id=1, ack='auto')

#conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')

time.sleep(2)
conn.disconnect()