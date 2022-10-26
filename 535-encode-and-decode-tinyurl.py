class Codec:
    mapping = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        idn = str(len(self.mapping))
        self.mapping[idn] = longUrl
        return 'http://tinyurl.com/' + idn

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.split('/')
        if len(shortUrl) == 4 and shortUrl[2] == 'tinyurl.com':
            idn = shortUrl[3]
        return self.mapping[idn]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))