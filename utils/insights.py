import numpy as np

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.cluster import KMeans
    SKLEARN_AVAILABLE = True
except:
    SKLEARN_AVAILABLE = False

class InsightEngine:
    def generate_insights(self, calc):
        insights = []
        insights.append(f"GPA: {calc.cumulative_gpa}")

        trend = calc.gpa_trend()
        if len(trend) > 2 and SKLEARN_AVAILABLE:
            X = np.arange(len(trend)).reshape(-1,1)
            y = np.array([g for _, g in trend])

            model = LinearRegression().fit(X, y)
            pred = model.predict([[len(trend)]])[0]

            insights.append(f"Predicted GPA: {round(pred,3)}")

        return insights