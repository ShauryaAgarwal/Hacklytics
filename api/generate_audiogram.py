class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Assuming post_data is JSON
        data = json.loads(post_data.decode('utf-8'))
        # Process data here to generate audiogram

        # Placeholder image URL
        image_url = "https://cdn.discordapp.com/attachments/1205691470951088199/1206234494667853844/image.png?ex=65db446a&is=65c8cf6a&hm=3c37da74d1ba751b4ac1e2918703bce7bbc6f069f597543caea600cae662fa4e&"

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({'audiogramImageUrl': image_url})
        self.wfile.write(response.encode())
