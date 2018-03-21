import urllib.request

opener = urllib.request.FancyURLopener({})
url = "https://www.hepsiburada.com/dell-gaming-7577-intel-core-i7-7700hq-8gb-1tb-128gb-ssd-gtx1050ti-freedos-15-6-fhd-ips-tasinabilir-bilgisayar-fb70d128f81c-p-HBV000009FDXO"
f = opener.open(url)
content = f.read()
str1=str(content)
splitTagOne = "\"originalPriceFormatted\":\"";
splitTagTwo = "\",\"unitPriceFormatted";
str1=str1.split(splitTagOne)[1];
#print(str1);
#print(str1.__len__());
str1=str1.split(splitTagTwo)[0];
print(str1);
#print(str1.__len__());
