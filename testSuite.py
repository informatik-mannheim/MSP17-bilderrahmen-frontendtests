from test_ionicapp import *
from test_ionicapp_webapp import *
from test_webapp import *



#---START OF SCRIPT
if __name__ == '__main__':
    # Uplaod multiple files is not working in Chrome Browser. Full Suite will use Firefox.
    # test webapp in Chrome with test_webapp.py (see the comments for skips)
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--browser', default='Firefox')
    #args = parser.parse_args()   
    
    #webapp_browser=args.browser
    #ionic_webapp_browser=args.browser
    #print("Testing with: "+args.browser)
    
    suite = unittest.TestLoader().loadTestsFromModule( sys.modules[__name__] )
    unittest.TextTestRunner(verbosity=2).run(suite)