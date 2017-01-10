## Program that counts the number of words in a sentence entered by a user
## By : Piranaven Selvathayabaran

def main():
    sentence=input("Enter a senctence : " )
    numwords=0
    words=sentence.split()
    for i in words:
        numwords= len(words)
    
    print("The number of words in your sentence is : ", numwords)

main()


        
    
    
