import sys
from spark import SparkApi
spark = SparkApi('M2U4MzQ3ZTYtZTczOC00YWQ4LTg3MzUtY2U0ODBmMTA2YWY0Y2ZmN2JjODUtZTFi')
TEST_USER = 'dchappell@charter.ca'

print "First, lets see if we can do anything..."
me_user = spark.people.get_me()
print "Success! My user ID is '" + me_user['id'] + "'"
print "Let's see what we can find out about myself..."
me_details = spark.people.get_detail(me_user['id'])
print "Looks like my name is '" + me_details['displayName'] + "'"
print "Lets see what rooms I'm in..."
rooms = spark.rooms.get(room_type='group')
for room in rooms:
    print room['title']
print "Let's see who I'm chatting with one-on-one"
rooms = spark.rooms.get(room_type='direct')
for room in rooms:
    print room['title']
print "Let's try to create a new room called 'PySpark Test'!"
room_id = spark.rooms.create('PySpark Test')
if not bool(room_id):
    print "Whoops! We hit an error trying to create a room. Exiting..."
    sys.exit(1)
print "Our room was created with id '" + room_id + "'"
print "let's try to add your test user to the room."
spark.memberships.create(room_id,p_email=TEST_USER, mod=True)
print "Your test user should now see the room"
garbage = raw_input("Press Enter to Continue...")
print "Let's post a message to the room!"
msg_id = spark.messages.create_in_room(room_id,"This is a message")
print "Check if you can see the message"
garbage = raw_input("Press Enter to Continue...")
print "Now, watch through the power of magic as the message dissapears!"
spark.messages.delete(msg_id)
garbage = raw_input("Press Enter to Continue...")
print "We will now delete that room we created..."
spark.rooms.delete(room_id)




