from lxml.builder import ElementMaker
from lxml import etree

NSMAP = {None: "http://doc.s3.amazonaws.com/2006-03-01", "tahoe": "http://doc.cryto.net/xml/tahoe-s3"}

E = ElementMaker(namespace="http://doc.s3.amazonaws.com/2006-03-01", nsmap=NSMAP)
Et = ElementMaker(namespace="http://doc.cryto.net/xml/tahoe-s3", nsmap=NSMAP)

buckets = (
	E.Bucket(
		E.Name("quotes"),
		E.CreationDate("2006-02-03T16:45:09.000Z"),
		Et.ReadCapability("ABC23423346"),
		Et.WriteCapability("H98NG3040S"),
		Et.VerifyCapability("3148J15990JE"),
	),
	E.Bucket(
		E.Name("samples"),
		E.CreationDate("2006-02-03T16:41:58.000Z")
	)
)

doc = E.ListAllMyBucketsResult(
	E.Owner(
		E.Id("bcaf1ffd86f461ca5fb16fd081034f"),
		E.DisplayName("webfile")
	),
	E.Buckets(
		*buckets
	)
)

print etree.tostring(doc, pretty_print=True)
