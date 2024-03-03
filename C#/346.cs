public class MovingAverage {

    private int maxSize;
    private double totalSum;
    private List<int> numbers;

    public MovingAverage(int size) {
        maxSize = size;
        totalSum = 0;
        numbers = new List<int>();
    }

    public double Next(int val) {

        if (numbers.Count == maxSize)
        {
            totalSum -= numbers[0];
            numbers.RemoveAt(0);
        }
        totalSum += val;
        numbers.Add(val);

        // double로 캐스팅 해야함
        return totalSum / numbers.Count;
    }
}
