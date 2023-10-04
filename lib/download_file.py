
import requests
import os
import sys
from urllib.parse import unquote

def download_file(file_link):

    #variables
    COMMON_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }

    #if you in increase this that will make less requests to server
    #but it will cause increase in memory
    CHUNK_SIZE = (1024 * 1024) * 2  # 2MB

    def generate_additional_headers(url_link):
        additional_headers = {}
        if url_link.endswith('.pdf'):
            additional_headers['Accept'] = 'application/pdf'
        elif url_link.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            additional_headers['Accept'] = 'image/*'
        elif url_link.endswith(('.mp4', '.avi', '.mkv')):
            additional_headers['Accept'] = 'video/*'
        elif url_link.endswith('.txt'):
            additional_headers['Accept'] = 'text/plain'
        return additional_headers

    def download(url_link, file_name, download_location=None):
        if not download_location:
            download_location = "./"

        print('[+] Downloading {} ...'.format(url_link))
        
        #headers
        headers = COMMON_HEADERS.copy()
        additional_headers = generate_additional_headers(url_link)
        headers.update(additional_headers)
        
        with open(download_location + file_name, 'wb') as f:
            try:
                response = requests.get(url_link, stream=True, headers=headers)
                total_length = response.headers.get('content-length')

                if total_length is None:  # no content length header
                    f.write(response.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=CHUNK_SIZE):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length) #comment this line to hide progress bar.
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done))) #comment this line to hide progress bar.
                        sys.stdout.flush() #comment this line to hide progress bar.
                print("\n")
                return True
            except requests.exceptions.SSLError:
                print("[-] SSL Error\n")
            except requests.exceptions.ConnectionError:
                print('[+] Peer Connection Reset ...')
        
        print('[+] Download Complete.')

    file_name = file_link.split('/')[-1]
    #you can specify the download_location, default is current dir
    download(file_link, file_name)

if __name__ == "__main__":
    file_link = "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_5mb.mp4"
    download_file(file_link)