import hashlib
import random

def generate_hash(attendee, event_name, event_url):
	string_to_hash = (event_name + "xx" + event_url + "xx" + attendee.first_name + "xx" + attendee.
		middle_name + "xx" + attendee.last_name + "xx" + attendee.college + "xx" + attendee.email + 
		"xx" + str(random.randint(1, 10**100))).encode(encoding = 'ASCII')

	return hashlib.sha256(string_to_hash).hexdigest()
