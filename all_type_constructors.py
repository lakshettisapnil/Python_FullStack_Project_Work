# class and object and constructore
class InstagramV1:
    def __init__(self,username):
        self.username = username 
        print(f'Hey {username} well come to instagram')
    def reels(self):
        print(f'You can see and scroll the reels')
    def posts(self):
        print(f'you can upload the pics')
class InstagramV2(InstagramV1):
    def __init__(self,username):
        super().__init__(username)
    def story(self):
        print("you can add story")
class InstagramV3(InstagramV2):
    def __init__(self,username):
        super().__init__(username)
    def note(self):
        print('You can add note')
class Live:
    def lunchlive(self):
        print('Now you can go on live')
class Verification:
    def verify(self):
        print('You can verify your account')
class InstagramV4(InstagramV3,Live,Verification):
    def __init__(self,username):
        super().__init__(username)
class Creator(InstagramV4):
    def insights(self):
        print("you can see your posts")
class Business(InstagramV4):
    def reach(self):
        print('you can see the reach')

sapnil = InstagramV1('swapnil')
sapnil.reels()
sapnil.posts()
praveen = InstagramV2('praveen')
praveen.reels()
praveen.posts()
praveen.story()

abhi = InstagramV3('abhi')
abhi.reels()
abhi.posts()
abhi.story()
abhi.note()

sham = InstagramV4('sham')
sham.reels()
sham.posts()
sham.story()
sham.note()
sham.lunchlive()
sham.verify() 

ram = Creator('sham')
ram.reels()
ram.posts()
ram.story()
ram.note()
ram.lunchlive()
ram.verify()
ram.insights() 

ravi = Business('ravi')
ravi.reels()
ravi.posts()
ravi.story()
ravi.note()
ravi.lunchlive()
ravi.verify()
ravi.reach()  