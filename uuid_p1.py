import uuid
import time

def uuid_poc():
 for x in range(10):
    start_time = time.time()


    # Generate a random UUID
    random_uuid = uuid.uuid4()
    print(f"{x} AAdhyAsri RAsAmAllA :-",random_uuid)
    end_time = time.time()
    print(f"Excution time {start_time - end_time }")

uuid_poc()



