import urllib.request
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument.")
        sys.exit(1)

    # Extract URL from command-line arguments
    url = sys.argv[1]

    # Send request and display X-Request-Id header value
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
