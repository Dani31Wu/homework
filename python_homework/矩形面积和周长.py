# User: link
# Date: 2023/9/9
# File: 矩形面积和周长

class Rectangle:

    @staticmethod
    def get_area(length, width):
        """
        获取面积
        :param length: 长度
        :param width: 宽度
        :return: area
        """
        area = length * width
        return area

    @staticmethod
    def get_perimeter(length, width):
        """
        获取周长
        :param length: 长度
        :param width: 宽度
        :return: perimeter
        """
        perimeter = 2 * (length + width)
        return perimeter


length_ = 8
width_ = 4
area_ = Rectangle.get_area(length_, width_)
perimeter_ = Rectangle.get_perimeter(length_, width_)
print(f"面积:{area_}, 周长:{perimeter_}")
