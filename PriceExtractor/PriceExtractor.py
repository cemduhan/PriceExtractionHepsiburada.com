import urllib.request

opener = urllib.request.FancyURLopener({})#creates a fancy url opener to parse the file
#url = "https://www.hepsiburada.com/dell-gaming-7577-intel-core-i7-7700hq-8gb-1tb-128gb-ssd-gtx1050ti-freedos-15-6-fhd-ips-tasinabilir-bilgisayar-fb70d128f81c-p-HBV000009FDXO"
url =  input("Please enter the url? ");
f = opener.open(url) #get the parsed page
content = f.read() #read the page into a variable
str1=str(content)   #convert it to str to easier search
splitTagOne = "\"originalPriceFormatted\":\""; #after digging a little in the file
splitTagTwo = "\",\"unitPriceFormatted";       #ı found that this is easy combination to extract the price
#"originalPriceFormatted":" SOMEPRICE ","unitPriceFormatted need to find part in between
str1=str1.split(splitTagOne)[1];#split in two and take second part
#print(str1);
#print(str1.__len__());
str1=str1.split(splitTagTwo)[0]; #do the same with rest but take the first part
print(str1);
#print(str1.__len__());
