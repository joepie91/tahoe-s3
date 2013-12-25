import hmac, hashlib, base64, urllib

pubkey = "AKIAIOSFODNN7EXAMPLE"
privkey = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def sign(key, message):
	return hmac.new(key, message.encode('utf-8'), hashlib.sha1).digest()

class S3SignatureGenerator(object):
        def set_keys(self, access_key, secret_key):
                self.access_key = access_key
                self.secret_key = secret_key
        
        def generate(self, verb, bucket, path, headers=[], content_md5="", content_type=""):
                date = ""
                
                elements = [
                        verb,
                        content_md5,
                        content_type,
                        date
                ]
                
                if len(headers) > 0:
                        elements.append(self.canonicalize_headers(headers))
                        
                elements.append(self.canonicalize_resource(bucket, path))
                
                sts = "\n".join()
                
        def canonicalize_resource(self, bucket=None, path="", subresources={}):
                # TODO: Multi-object DELETE parameter?
                if bucket is None:
                        result = "/%s/" % path
                else:
                        result = "/%s%s" % (bucket, path)
                
                if len(subresources) > 0:
                        subresources = sorted(subresources.items())
                        subresource_strings = []
                        
                        for subresource, value in subresources:
                                if subresource in ("acl", "lifecycle", "location", "logging", "notification", "partNumber", "policy", "requestPayment", "torrent", "uploadId", "uploads", "versionId", "versioning", "versions", "website"):
                                        if value is None:
                                                subresource_strings.append(subresource)
                                        else:
                                                # Not sure if this is a correct implementation of the encoding...
                                                if subresource not in ("response-content-type", "response-content-language", "response-expires", "response-cache-control", "response-content-disposition", "response-content-encoding"):
                                                        value = urllib.quote(str(value))
                                                        
                                                subresource_strings.append("%s=%s" % (subresource, value))
                        
                        if len(subresource_strings) > 0: # Don't add this if there were no qualifying subresource specifiers
                                result += "?%s" % "&".join(subresource_strings)
                        
                return result
                
        def canonicalize_headers(self, ):
                pass
                
        def sign(self, sts):
                return base64.b64encode(hmac.new(self.secret_key, sts.encode("utf-8"), hashlib.sha1).digest())

s = S3SignatureGenerator()
print s.canonicalize_resource("testbucket", "/test/path", subresources={"torrent": None, "abc-id": 4})

#print "AWS %s:%s" % (pubkey, base64.b64encode(sign(privkey, sts)))
