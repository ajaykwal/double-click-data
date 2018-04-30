import argparse
import random
import json
import ImpressionRecord as Impr


if __name__== "__main__":
    LOCATION_FILE = 'loc.json'
    DEVICE_FILE='dev.json'
    HEADER= "Time,UserId,AdvertiserId,OrderId,LineItemId,CreativeId,CreativeVersion,CreativeSize,AdUnitId,CustomTargeting,Domain,CountryId,Country,RegionId,Region,MetroId,Metro,CityId,City,PostalCodeId,PostalCode,BrowserId,Browser,OSId,OS,OSVersion,BandwidthId,BandWidth,TimeUsec,AudienceSegmentIds,Product,RequestedAdUnitSizes,BandwidthGroupId,MobileDevice,MobileCapability,MobileCarrier,IsCompanion,TargetedCustomCriteria,DeviceCategory,IsInterstitial,EventTimeUsec2,YieldGroupNames,YieldGroupCompanyId,MobileAppId,RequestLanguage,DealId,DealType,AdxAccountId,SellerReservePrice,Buyer,Advertiser,Anonymous,ImpressionId"
    record_layout=HEADER.split(',')
    parser = argparse.ArgumentParser()
    parser.add_argument('--records',
                  dest='records',
                  default=100,
                  help='number of records')
    parser.add_argument('--output',
                  dest='output',   
                  help='Output file to write results to.')
    parser.add_argument('--filecount',
                        dest='filecount',
                        help='number of files')
    parser.add_argument('--fileprefix',
                  dest='fileprefix',   
                  help='prefix of the files')
    parser.add_argument('--startdate',
                  dest='startdate',
                  help='start date')
    parser.add_argument('--enddate',
                        dest='enddate',
                        help='end date')

    options, args = parser.parse_known_args(args=None, namespace=None)
    print options

    with open(LOCATION_FILE) as l:
        locs=json.load(l)

    with open(DEVICE_FILE) as d:
        devs=json.load(d)

    location=random.choice(locs['locations'])
    device=random.choice(devs['devices'])

    print options.filecount

    for i in range(0,int(options.filecount)):
        filename=options.fileprefix+options.startdate+"_"+str(i)
        print "Filename "+filename
        with open(filename,'w',1) as outfile:
            outfile.write(HEADER)
            for x in range(1,int(options.records)):
                impression=Impr.ImpressionRecord(location, device, options.startdate, options.enddate, record_layout)
                outfile.write(impression.getrecord())

