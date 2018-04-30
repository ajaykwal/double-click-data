import random
import time
import string


class ImpressionRecord:

    advinfo=["128436289,9832456,123450,Macys",
              "128436289,9832457,123451,Macys",
                          "128436289,9832458,123452,Macys",
                          "128436290,9832556,123453,Udemy",
                          "128436290,9832557,123454,Udemy",
                          "128436290,9832558,123455,Udemy",
                          "128436290,9832559,123456,Udemy ",
                          "128436291,9832661,123457,Disney",
                          "128436291,9832662,123458,Disney",
                          "128436291,9832663,123459,Disney"]

    creative_sizes = ['100x100','300x250','600x600','970x250']

    def initData(self):
        self.record['Time'] = time.strftime('%Y-%m-%d %H:%M:%S',
                                       time.localtime(random.randrange(self.startDateTime, self.endDateTime)))

        self.record['UserId'] = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(15))
        self.record['AdvertiserId'], self.record['OrderId'], self.record['LineItemId'], self.record['Advertiser'] = random.choice(
            self.advinfo).split(',')
        self.record['CreativeId'] = str(random.randint(3340045, 3340045))
        self.record['CreativeVersion'] = str(random.randint(0, 2))
        self.record['CreativeSize'] = random.choice(self.creative_sizes)
        self.record['AdUnitId'] = str(random.randint(96218817, 96218817))
        self.record['CustomTargeting'] = ""
        self.record['Domain'] = ""
        self.record['CountryId'] = self.location['CountryId']
        self.record['Country'] = self.location['Country']
        self.record['RegionId'] = self.location['RegionId']
        self.record['Region'] = self.location['Region']
        self.record['MetroId'] = self.location['MetroId']
        self.record['Metro'] = self.location['Metro']
        self.record['CityId'] = self.location['CityId']
        self.record['City'] = self.location['City']
        self.record['PostalCodeId'] = self.location['PostalCodeId']
        self.record['PostalCode'] = self.location['PostalCode']
        self.record['BrowserId'] = self.device['BrowserId']
        self.record['Browser'] = self.device['Browser']
        self.record['OSId'] = self.device['OSId']
        self.record['OS'] = self.device['OS']
        self.record['OSVersion'] = self.device['OSVersion']
        self.record['BandwidthId'], self.record['BandWidth']=random.sample({'502002': 'Cable', '502018': 'adsl2-12mbps', '502004': 'Cellular'}.items(), 1)[0]
        self.record['TimeUsec'] = str(random.randint(1501697172, 1501697272))
        self.record['AudienceSegmentIds'] = '1966|67396|70396|210076|210796|632476|699316|833605'
        self.record['Product'] = random.choice(["First Look", "Ad Exchange"])
        self.record['RequestedAdUnitSizes'] = 'fluid|320x50|320x120|320x180|300x250'
        self.record['BandwidthGroupId'] = random.choice(["4", "3"])
        self.record['MobileDevice'] = self.device['MobileDevice']
        self.record['MobileCapability'] = random.choice(["Mobile Apps", "Mobile Games"])
        self.record['MobileCarrier'] = random.choice(["AT&T", "Verizon", "Sprint"])
        self.record['IsCompanion'] = 'FALSE'
        self.record['TargetedCustomCriteria'] = 'x=foo'
        self.record['DeviceCategory'] = random.choice(["Smartphone", "Tablet", "Laptop"])
        self.record['IsInterstitial'] = 'FALSE'
        self.record['EventTimeUsec2'] = str(random.randint(1506541836179249, 1506541836199249))
        self.record['YieldGroupNames'] = 'alvinc_web_deal_pd_GOLDEN'
        self.record['YieldGroupCompanyId'] = '154939609'
        self.record['MobileAppId'] = random.choice(["com.google.android.youtube", "com.google.ios.youtube"])
        self.record['RequestLanguage'] = random.choice(["en", "es"])
        self.record['DealIdrecord'] = random.choice(["web_deal_pd_v0", "web_deal_pd_v1"])
        self.record['DealType'] = "Preferred deal"
        self.record['DealId'] = "Deal Id"
        self.record['AdxAccountId'] = random.choice(["128436289", "128436389"])
        self.record['SellerReservePrice'] = random.choice(["0.004999", "0.005999"])
        self.record['Buyer'] = "Steeman  Network"
        self.record['Advertiser'] =""
        self.record['Anonymous']=""
        self.record['ImpressionId'] = (random.randint(1234567890, 2234567890))

    def __init__(self,loc, dev, start, end, record_layout):
        start_date=str(start)+" 01:00:00"
        end_date=str(end)+" 23:59:00"
        self.startDateTime = time.mktime(time.strptime(start_date, '%b-%d-%Y %H:%M:%S'))
        self.endDateTime = time.mktime(time.strptime(end_date, '%b-%d-%Y %H:%M:%S'))
        self.location=loc
        self.device=dev
        self.record_layout=record_layout
        self.record = {}
        self.initData()

    def getrecord(self):
        rec=""
        first = True
        for x in self.record_layout:
            if first:
                first = False
                rec = str(self.record[x])
            else:
                rec = rec + ","+ str(self.record[x])
        return rec


