# -*- coding:utf8 -*-
import time

head = """#EXTM3U
#EXT-X-VERSION:3
#EXT-X-MEDIA-SEQUENCE:{sequence}
#EXT-X-ALLOW-CACHE:YES
#EXT-X-TARGETDURATION:10
"""

ts_list = []
max_ts_index = 22

absolute_path = "http://localhost:8888/get_ts/"

def init_ts_list():
    global ts_list
    ts_list = [0, 1, 2]


def change_index2str(ts_index, prex="abc", zero_max=3, play_sec=10):
    play_sec_desc = "#EXTINF:%s,\n" % (str(play_sec))
    ts_desc = prex + "0" * (zero_max - len(str(ts_index))) + str(ts_index) + ".ts\n"
    ts_desc = absolute_path + ts_desc
    return "%s%s" % (play_sec_desc, ts_desc)


def get_rewrite_content():
    content = ""
    for ts_index in ts_list:
        content += change_index2str(ts_index)
    return "%s\n%s" % (head.format(sequence=ts_list[0]), content)


def update_list():
    if ts_list[-1] >= max_ts_index:
        print "ts_list init"
        init_ts_list()
    else:
        # ts_list.append(ts_list[-1] + 1)
        for i in range(len(ts_list)):
            ts_list[i] += 1


def live(interval=10, m3u8_file="./static/video_data/test.m3u8"):
    """
        @description: monitor live continue
    """
    while ts_list[-1] <= max_ts_index:
        content = get_rewrite_content()
        print content
        with open(m3u8_file, "wb") as fs:
            fs.write(content)
        time.sleep(interval)
        update_list()


if __name__ == "__main__":
    init_ts_list()
    live(interval=10, m3u8_file="./static/video_data/test.m3u8")
