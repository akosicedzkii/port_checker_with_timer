import stomp
import time
import send_email
import logging

class SampleListener(object):
  def on_message(self, headers, msg):
    send_email.send_message(msg)
    print(msg)
    
while True: 
    conn = stomp.Connection10()
    
    conn.set_listener('SampleListener', SampleListener())
    
    conn.start()
    
    conn.connect()
    
    conn.subscribe('test')
    
    time.sleep(1) # secs
    
    conn.disconnect()