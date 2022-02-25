import random
class MyApp:
    def __init__(self):
        self.bill={}
        self.movies={
			'bollywood':['1.Bellbottom',
			             '2.Chehre',
			             '3.Thalaivii',
			             '4.Tadap',
			             '5.RRR',
			             '6.Maidaan',
			             '7.Prithviraj',
			             '8.Jersey',
			             '9.No means No',
			             '10.Bachchan Pandey',
			             '11.Sherahaah',
			             '12.83',
			             '13.Sooryavanshi',
			             '14.Tejas'],
			             
			'hollywood':['1.Eternals',
			             '2.No Time To Die',
			             '3.Morbius',
			             '4.Spider Man:No Way Home',
			             '5.Thor:Love and Thunder'],
			             
			'tollywood':['1.Pakka Commercial',
			             '2.RRR'],
			             
			'animation':['1.Sing 2 ',
			             '2.Encanto',
			             '3.Minions:The Rise of Guru'],

			'anime'	:['1.My Hero Academia:World Hero Misson',
			          '2.Sword Art Online:Progressive Aria of a Starless Night']
		}
		
        print("------------PROJECT BY ALOK,ABHIGYAN,ANNAMIKA AND AMAN------------")
        print("------------Book Your Show----------")
        print("Hello",input("enter your name : "))
        print('SELECT MOVIE TYPE : 1.Bollywood 2.Hollywood 3.Tollywood 4.Animation 5.Anime')
        ch=int(input(' > '))
        if ch==1:
            self.bill['category']='bollywood'
            self.Movies(self.movies['bollywood'])
        elif ch==2:
            self.bill['category']='hollywood'
            self.Movies(self.movies['hollywood'])
        elif ch==3:
            self.bill['category']='tollywood'
            self.Movies(self.movies['tollywood'])
        elif ch==4:
            self.bill['category']='animation'
            self.Movies(self.movies['animation'])
        elif ch==5:
            self.bill['category']='anime'
            self.Movies(self.movies['anime'])
        else:
            print('INVALID OPTION CHOOSEN !')
				
    def buy(self):
        print("1.Balcony=Rs.180 2.Classic=Rs.140 3.Special=Rs.220")
        ch=int(input("Type your choice:"))
        if ch==1:
            self.bill['seat']='Balcony'
        elif ch==2:
            self.bill['seat']='Classic'
        elif ch==3:
            self.bill['seat']='Special'
            
        def buy_ticket(ticketcash):
            a=int(input("enter number of seats="))
            b=ticketcash
            c=a*b
            print(c)
            print("How would you like to pay")
            print("1.Phone Pe 2.Google Pay 3.Amazone Pay 4.Net Banking 5.Pay at counter")
            ch=int(input("Type your choice:"))
            notation="Pay to this number 9170946871.Tickets would be send to your mobile as a message.\nIf not money would be send back in short time"
            if ch==1:
                print(notation)
            elif ch==2:
                print(notataion)
            elif ch==3:
                print(notation)
            elif ch==4:
                a=int(input("enter account number"))
                b=int(input("enter amount of money"))
                print("Amount Recived")
                print("Tickets would be send to your mobile as a message.")
                print("If not money would be send back in short time")
            elif ch==5:
                print("Tickets would be given at counter")
            else:
                print('INVALID OPTION SELECTED !')
        if ch==1:
            self.bill['price']=180
            buy_ticket(180)
        elif ch==2:
            self.bill['price']=140
            buy_ticket(140)
        elif ch==3:
            self.bill['price']=220
            buy_ticket(220)
        else:
            print('INVALID OPTION CHOOSEN !')

    def vaccination(self):
        print("---------ARE YOU VACCINATED----------")
        a=input("enter your choice YES or NO = ")
        if a.lower()=="yes":
            print("------Good To Go--------")
        else:
            print("----------First Get Vaccinated-----------")
            a=input("enter your name= ")
            b=int(input("enter your mobile number= "))
            c=int(input("enter your age= "))
            print("You are sheduled to be vaccinated on 5 october 2021")
            print("Place = Near Chota Imambara")
            print(" PIN =",random.randint(100,1000))

    def print_(self,list):
        for i in list:
            print('\t'+str(i))
            
    def makebill(self):
        print(''' 
             -------------- TICKET ---------------
	             • BOOK MY SHOW MANAGEMENT •       
            
	           MOVIE NAME : {0}
	           CATEGORY   : {1}
	           SEAT       : {2}
	           PRICE      : ₹{3}
	           HALLNAME   : {4}
	        -------------------------------------'''.format(self.bill['movie'],
	                                                     self.bill['category'],
	                                                     self.bill['seat'],
	                                                     self.bill['price'],
	                                                     self.bill['hall']))
    def Movies(self,movies):
        print("<< Top Showing >>")
        self.print_(movies)
        ch=int(input("Type your choice:"))
        self.bill['movie']=movies[ch-1].split('.')[1]
        print("<< Halls near You >>")
        halls='1.Novelty-Aligang 2.Novelty-Lalbagh 3.Sahu-Cinemas 4.Wave-The-Mall 5.Inox 6.PVR-Cinemas 7.Cinepolis-Cinemas 8.Pratibha-Theater 9.Shubham-Cinemas 10.Fun-Cinemas'.split()
        self.print_(halls)
        ch=int(input("Type your choice:"))
        self.bill['hall']=halls[ch-1].split('.')[1]
        self.vaccination()
        self.buy()
        self.makebill()
		
MyApp()