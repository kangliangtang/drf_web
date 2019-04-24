
# name = 'ssssssss'
# try:
#     name = 'kkk'
# except Exception:
#     pass
# finally:
#     print(name)


# from django.utils import timezone
# import pytz
# import datetime
# import time
#
# # start_time_str  = '2019-04-19 10:08:00'
# start_time_str  = datetime.datetime.now()
# start_time_str  = time.time()
# start_time_str  = '2017-04-23T05:27:20.000Z'
# start_time_str  = '2019-04-19T09:10:20.000Z'
# print('=====', start_time_str)
# start_time = timezone.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc)
# print('----', start_time)



def test(id):
    print(id)
    try:
        n = id +''
    except Exception:
        pass


s = test(2)
print(s)