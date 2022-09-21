import cv2
import cv2.aruco as aruco



       


def CharucoBoard(squaresX=5, squaresY=5, squareLength=0.008, markerLength=0.006,
                 marker_size=4,total_markers=250):

    key = getattr(aruco,f'DICT_{marker_size}X{marker_size}_{total_markers}')          # Creates a custermizable key in the format arruco.DICT_4X4_1000
    arucoDict = aruco.Dictionary_get(key)
    Board = aruco.CharucoBoard.create(squaresX,squaresY,squareLength,markerLength,arucoDict)
    img3 = aruco.CharucoBoard.draw(Board,outSize=(640,480),marginSize =30,borderBits = 1)
    cv2.imwrite("BOARD.png",img3)
    cv2.waitKey(0)    
    
def main():
    CharucoBoard()

if __name__ == '__main__':
    main()