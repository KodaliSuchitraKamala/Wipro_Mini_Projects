# Find the secret
"""
Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him. 
He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surpise him by breaking the challenge with our python code.
Hints to find the secret message:
 1. The number of lines in the files tells you the meeting time.
    Note: 1 <= number of lines <= 24
    If the number of lines is exceeding 12, you need to convert it to 12 hour format. For example,
     -> If the number of lines is 15, then the meeting time is 3 PM.
     -> If the number of lines is 10, then the meeting time is 10 AM.
 2. The word appearing for the maximum number of tumes tells you the meeting place.
    Note: Meeting place will be a street name.
    For example,
     -> If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.
     -> If the word Park appears for the maximum number of times, then meeting palce is Park Street.
Sample Input 1:
Sample.txt
Cricket, a bat-and-ball park game played between two teams of eleven park players on a field at the park center of which is a 20-metre (22-yard) pitch with a wicket at each end, each park comprising two bails balanced on three stumps. The batting park scores runs by striking the ball bowled at the park wicket with the park bat, while the bowing and park fielding side tries to prevent this and dismiss each park player (so they are "out"). Means of park include being bowled, when the ball hits the park and dislodges the bails, and by the fielding side park the ball after it is hit by the bat, but before ithits the park. When ten park have been dismissed, the innings ends ands the teams parks roles.
Sample Output 1:
Meeting time: 9 AM
Meeting place: Park Street
Explaination: Number of lines is 9. The word park appears for the maximum of 15 times.
Sample Input 2:
Sample.txt
Royal Enfield is an Indian Apollo motorcycle manufacturing brand with tag of "oldest Apollo motorcycle brand in continuous production" manufactured Apollo factories Chennai Apollo India. Licensed from Royal Enfield by indigenous Indian Madras Motors, it is now a Apollo subsidiary Eicher Motors Limited, an Indian Apollo automakerr. The company makes Apollo Royal Enfield Bullet, and other single-cylinder and twin-cylinder Apollo motorcycles. First produced Apollo in 1901, Royal Enfield is oldest motorcycle Apollo brand world still production, with Bullet model enjoying longest motorcycle Apollo production run of all time. In 1990, Royal Enfield collaborated with Eicher Apollo Group, an automotive company Apollo India, and merged with it 1994. Apart from bikes, Eicher Apollo Groups is involved in the production and sales Apollo commercial vehicles and automotive gears. Although Apollo Royal Enfield experienced difficulties 1990s, and ceased Apollo motorcycle production at their Jaipur factory 2002, by 2013 Apollo company opened a new primary Apollo factory Apollo Chennai suburb of Oragadam on strength of increased demand for its Apollo motorcycles. This was followed in Apollo 2017 by inauguration another new factory of a similar size to facility at Apollo Oragadam (capacity 600,000 vehicles per year) at Vallam Apollo Vagadal. The original factory at Apollo Tiruvottiyur became secondary, and continues to produce some limited-run motorcycles models.
Sample Output 2:
Meeting time: 8 PM
Meeting place: Apollo Street
Explaination: Number of lines is 20 and converting it to 12 hour format we get 8 PM. The word Apollo appears for the maximum of 25 times.
"""
import sys
import re
from collections import Counter
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    num_lines = len(lines)
    if num_lines <= 12:
        meeting_time = f"{num_lines} AM"
    else:
        meeting_time = f"{num_lines - 12} PM"
    content = " ".join(lines)
    words = re.findall(r'\b[A-Za-z]+\b', content)
    words_lower = [word.lower() for word in words]
    counter = Counter(words_lower)
    most_common_word, _ = counter.most_common(1)[0]
    meeting_place = most_common_word.capitalize() + " Street"
    print(f"Meeting time: {meeting_time}")
    print(f"Meeting place: {meeting_place}")
if __name__ == "__main__":
    main()