import sys
import argparse
import os.path


def byte_frames_from_file(movie):
    "Generate frame data from DTM movie."


def text_frames_from_bytes(frame_data):
    "Convert DTM frame data to text."


def main(argv=None):
    if argv is None:
        argv = sys.argv

    description = ('DTM <-> plain text')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('movie', help='the DTM to dump')

    args = parser.parse_args(argv[1:])

    movie_path = args.movie
    movie_basename = os.path.basename(movie_path)
    header_bytes = 256
    header_path = "{}_header".format(movie_basename)
    frames_path = "{}_frames.txt".format(movie_basename)

    with open(movie_path, mode='rb') as bin_movie_file:
        with open(header_path, mode='wb') as bin_header_file:
            with open(frames_path, mode='w') as text_frames_file:
                # Advance the movie past the header.
                header_bytes = bin_movie_file.read(header_bytes)

                # Parse the frame data.
                byte_frames = byte_frames_from_file(bin_movie_file)
                text_frames = text_frames_from_bytes(byte_frames)

                # Write the results.
                bin_header_file.write(header_bytes)
                for text_frame in text_frames:
                    text_frames_file.write(text_frame + "\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
