import sys
import argparse
import os.path
import struct


def byte_frames_from_file(movie):
    "Generate frame data from DTM movie."
    frame_bytes = 8
    while True:
        frame = movie.read(frame_bytes)
        if not frame:
            break
        yield frame


def text_frame_from_bytes(frame_data):
    "Convert DTM frame data to text."
    flags, l, r, a_x, a_y, c_x, c_y = struct.unpack("H6B", frame_data)
    start_flag = flags & 1
    a_flag = flags >> 1 & 1
    b_flag = flags >> 2 & 1
    x_flag = flags >> 3 & 1
    y_flag = flags >> 4 & 1
    z_flag = flags >> 5 & 1
    d_up = flags >> 6 & 1
    d_down = flags >> 7 & 1
    d_left = flags >> 8 & 1
    d_right = flags >> 9 & 1
    l_flag = flags >> 10 & 1
    r_flag = flags >> 11 & 1
    button_data = (start_flag, a_flag, b_flag, x_flag, y_flag,
                   z_flag, d_up, d_down, d_left, d_right, l_flag,
                   r_flag, l, r, a_x, a_y, c_x, c_y)
    return ":".join(str(b) for b in button_data)


def byte_frame_from_text(frame_data):
    "Convert text frame data to DTM."
    if frame_data == '\n':
        result = b''
    elif frame_data[0] == '#':
        result = b''
    else:
        start_flag, a_flag, b_flag, x_flag, y_flag, z_flag, d_up, d_down, d_left, d_right, l_flag, r_flag, l, r, a_x, a_y, c_x, c_y = (int(b) for b in frame_data.split(":"))
        flags = r_flag
        flags = flags << 1 | l_flag
        flags = flags << 1 | d_right
        flags = flags << 1 | d_left
        flags = flags << 1 | d_down
        flags = flags << 1 | d_up
        flags = flags << 1 | z_flag
        flags = flags << 1 | y_flag
        flags = flags << 1 | x_flag
        flags = flags << 1 | b_flag
        flags = flags << 1 | a_flag
        flags = flags << 1 | start_flag
        result = struct.pack("H6B", flags, l, r, a_x, a_y, c_x, c_y)
    return result


def text2dtm(argv=None):
    if argv is None:
        argv = sys.argv

    description = ('Convert header + plain text frame data to DTM.')
    parser = argparse.ArgumentParser(description=description,
                                     fromfile_prefix_chars='@')
    parser.add_argument('output', help='output file name')
    parser.add_argument('header', help='256 byte header file')
    parser.add_argument('frames', nargs='+',
                        help='one file of frame data;'
                        ' prefix with @ to use a from-file')

    args = parser.parse_args(argv[1:])

    movie_path = args.output
    header_path = args.header
    frame_paths = args.frames

    with open(movie_path, mode='wb') as bin_movie_file:
        with open(header_path, mode='rb') as bin_header_file:
            bin_movie_file.write(bin_header_file.read())
        for frame_path in frame_paths:
            with open(frame_path, mode='r') as text_frames_file:
                for text_frame in text_frames_file:
                    byte_frame = byte_frame_from_text(text_frame)
                    bin_movie_file.write(byte_frame)

    return 0


def dtm2text(argv=None):
    if argv is None:
        argv = sys.argv

    description = ('Convert DTM to header file + plain text frame data.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('movie', help='the DTM to dump')

    args = parser.parse_args(argv[1:])

    movie_path = args.movie
    movie_basename = os.path.basename(movie_path)
    header_bytes = 256
    header_path = "{}_header".format(movie_basename)
    frames_path = "{}_frames.txt".format(movie_basename)

    with open(movie_path, mode='rb') as bin_movie_file:
        # This has the side effect of advancing the movie file.
        # That's a good thing in our case.
        header_bytes = bin_movie_file.read(header_bytes)

        with open(header_path, mode='wb') as bin_header_file:
            bin_header_file.write(header_bytes)

        with open(frames_path, mode='w') as text_frames_file:
            for byte_frame in byte_frames_from_file(bin_movie_file):
                text_frame = text_frame_from_bytes(byte_frame)
                text_frames_file.write(text_frame + "\n")

    return 0


if __name__ == '__main__':
    sys.exit(dtm2text())
