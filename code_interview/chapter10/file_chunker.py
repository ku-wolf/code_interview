#!/usr/bin/python3
import os

def get_chunks(file_size, chunk_size):
    chunk_start = 0
    while chunk_start + chunk_size < file_size:
        yield(chunk_start, chunk_size)
        chunk_start += chunk_size

    final_chunk_size = file_size - chunk_start
    yield(chunk_start, final_chunk_size)

def read_file_chunked(file_path, chunk_size):
    with open(file_path, "rb") as file_:
        file_size = os.path.getsize(file_path)

        print('File size: {}'.format(file_size))

        progress = 0

        for chunk_start, chunk_size in get_chunks(file_size, chunk_size):

            file_chunk = file_.read(chunk_size)

            progress += len(file_chunk)
            yield(file_chunk)

            print('{0} of {1} bytes read ({2}%)'.format(
                progress, file_size, int(progress / file_size * 100))
            )

if __name__ == "__main__":
    for chunk in read_file_chunked("test"):
        pass
