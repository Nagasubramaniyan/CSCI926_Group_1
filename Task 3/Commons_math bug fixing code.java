public class Bug_fixing {
    // MATH-482
    public static float max(final float a, final float b) {
        return (a <= b) ? b : (Float.isNaN(a + b) ? Float.NaN : a);
    }

    // MATH-288
    private Integer getPivotRow(final int col, final SimplexTableau tableau) {
        double minRatio = Double.MAX_VALUE;
        Integer minRatioPos = null;
        for (int i = tableau.getNumObjectiveFunctions(); i < tableau.getHeight(); i++) {
            final double rhs = tableau.getEntry(i, tableau.getWidth() - 1);
            final double coeff = tableau.getEntry(i, col);
            if (MathUtils.compareTo(coeff, 0, epsilon) > 0) {
                final double ratio = rhs / coeff;
                final int cmp;
                cmp = Double.compare(ratio, minRatio);
                if (cmp < 0) {
                    minRatio = ratio;
                    minRatioPos = i;
                } else if (cmp == 0) {
                    minRatioPos = i;
                }
            }
        }
        return minRatioPos;
    }

    // MATH-305
    public static double distance(int[] p1, int[] p2) {
        double sum = 0;
        for (int i = 0; i < p1.length; i++) {
            final double dp = p1[i] - p2[i];
            sum += dp * dp;
        }
        return Math.sqrt(sum);
    }

    // MATH-482
    public double evaluate(double x, double epsilon, int maxIterations) {

        double p1 = getA(0, x);
        double q1 = 0.0;
        int n = 1;
        double cp = p1;
        double hN = p1;

        while (n<maxIterations){
            final double a = getA(n,x);
            final double b = getB(n,x);
            double d = a+b* q1;
            double c = a+b/ cp;
            d = 1 / d;
            final double deltaN = c * d;
            hN = p1 * deltaN;
            q1 = d;
            cp = c;
            p1 = hN;
            n++;
        }
}
