def stress_prediction(alpha, beta, gamma):
    if beta > alpha and beta > gamma:
        return "High Stress"
    elif alpha > beta:
        return "Relaxed"
    else:
        return "Normal"
    