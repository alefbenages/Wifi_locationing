{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ba38ce88-5dab-400f-966d-ab22af6f984d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def makePredictionsFromLoadedModels (loaded_model, X_test, y_test):\n",
    "    model_predictions = loaded_model.predict(X_test)\n",
    "\n",
    "    print(accuracy_score(y_test, model_predictions))\n",
    "    print(confusion_matrix(y_test, model_predictions))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
