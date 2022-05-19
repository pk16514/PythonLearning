"""
--> Draw a Line

Syntax: cv2.line(image, start_point, end_point, color, thickness)
Parameters:
        image: It is the image on which line is to be drawn.
        start_point: It is the starting coordinates of line. The coordinates are represented as
                     tuples of two values i.e. (X coordinate value, Y coordinate value).
        end_point: It is the ending coordinates of line. The coordinates are represented as tuples
                   of two values i.e. (X coordinate value, Y coordinate value).
        color: It is the color of line to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for
               blue color.
        thickness: It is the thickness of the line in px.
        Return Value: It returns an image.

--> Draw Arrow Segment

Syntax: cv2.arrowedLine(image, start_point, end_point, color[, thickness[, line_type[, shift[, tipLength]]]])
Parameters:
        image: It is the image on which line is to be drawn.
        start_point: It is the starting coordinates of line. The coordinates are represented as tuples
                     of two values i.e. (X coordinate value, Y coordinate value).
        end_point: It is the ending coordinates of line. The coordinates are represented as tuples of
                   two values i.e. (X coordinate value, Y coordinate value).
        color: It is the color of line to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
        thickness: It is the thickness of the line in px.
        line_type: It denotes the type of the line for drawing.
        shift: It denotes number of fractional bits in the point coordinates.
        tipLength: It denotes the length of the arrow tip in relation to the arrow length.
        Return Value: It returns an image.

--> Draw An Ellipse

Syntax: cv2.ellipse(image, centerCoordinates, axesLength, angle, startAngle, endAngle, color [, thickness[, lineType[, shift]]])
Parameters:
        image: It is the image on which ellipse is to be drawn.
        centerCoordinates: It is the center coordinates of ellipse. The coordinates are represented as
                           tuples of two values i.e. (X coordinate value, Y coordinate value).
        axesLength: It contains tuple of two variables containing major and minor axis of ellipse
                    (major axis length, minor axis length).
        angle: Ellipse rotation angle in degrees.
        startAngle: Starting angle of the elliptic arc in degrees.
        endAngle: Ending angle of the elliptic arc in degrees.
        color: It is the color of border line of shape to be drawn. For BGR, we pass a tuple.
               eg: (255, 0, 0) for blue color.
        thickness: It is the thickness of the shape border line in px. Thickness of -1 px will fill the
                   shape by the specified color.
        lineType: This is an optional parameter.It gives the type of the ellipse boundary.
        shift: This is an optional parameter. It denotes the number of fractional bits in the coordinates of the center and values of axes.
        Return Value: It returns an image.

--> Draw a Circle

Syntax: cv2.circle(image, center_coordinates, radius, color, thickness)
Parameters:
        image: It is the image on which circle is to be drawn.
        center_coordinates: It is the center coordinates of circle. The coordinates are represented as
                            tuples of two values i.e. (X coordinate value, Y coordinate value).
        radius: It is the radius of circle.
        color: It is the color of border line of circle to be drawn. For BGR, we pass a tuple.
               eg: (255, 0, 0) for blue color.
        thickness: It is the thickness of the circle border line in px. Thickness of -1 px will fill
                   the circle shape by the specified color.
        Return Value: It returns an image.

--> Draw a Rectangle

Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
Parameters:
        image: It is the image on which rectangle is to be drawn.
        start_point: It is the starting coordinates of rectangle. The coordinates are represented as
                     tuples of two values i.e. (X coordinate value, Y coordinate value).
        end_point: It is the ending coordinates of rectangle. The coordinates are represented as tuples
                   of two values i.e. (X coordinate value, Y coordinate value).
        color: It is the color of border line of rectangle to be drawn. For BGR, we pass a tuple.
               eg: (255, 0, 0) for blue color.
        thickness: It is the thickness of the rectangle border line in px. Thickness of -1 px will fill
                   the rectangle shape by the specified color.
        Return Value: It returns an image.

--> Draw a Text String

Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
Parameters:
        image: It is the image on which text is to be drawn.
        text: Text string to be drawn.
        org: It is the coordinates of the bottom-left corner of the text string in the image. The
             coordinates are represented as tuples of two values i.e. (X coordinate, Y coordinate).
        font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN etc.
        fontScale: Font scale factor that is multiplied by the font-specific base size.
        color: It is the color of text string to be drawn.
        thickness: It is the thickness of the line in px.
        lineType: This is an optional parameter.It gives the type of the line to be used.
        bottomLeftOrigin: This is an optional parameter. When it is true, the image data origin is at
                          the bottom-left corner. Otherwise, it is at the top-left corner.
        Return Value: It returns an image.
"""

import cv2

image = cv2.imread('pp2.jpg')
image = cv2.line(image, (0, 0), (250, 250), (0, 255, 0), 9)
image = cv2.arrowedLine(image, (225, 0), (0, 90), (0, 0, 255), 9, tipLength=0.5)
image = cv2.ellipse(image, (500, 500), (100, 50), 0, 0, 360, (0, 0, 255), 5)
image = cv2.circle(image, (800, 500), 20, (255, 0, 0), -1)
image = cv2.rectangle(image, (350, 350), (800, 500), (0, 255, 0), 4)
image = cv2.putText(image, 'OpenCV', (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('Image', image)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
