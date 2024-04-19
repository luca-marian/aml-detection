# Algorithms
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier

from utils import print_metrics


def test_traditional_algorithms():
    for Name, cls in pipeline_cls.items():
        cls.fit(X_train, y_train)
        y_proba = cls.predict_proba(X_test)
        y_pred = (y_proba[:, 1] >= threshold).astype(int)

        print(Name)
        print(cls)
        print("Metrics for " + str(Name) + "\n")
        print(classification_report(y_test, y_pred))

        print_metrics(y_pred, y_test, Name + " - MD ")

        if f1_score(y_test, y_pred, average="macro") > base_f1_score:
            base_f1_score = f1_score(y_test, y_pred, average="macro")
            best_model = cls
            best_model_name = Name

        print(
            "-----------------------------------------------------------------------------------------------------------------------"
        )

    return best_model, best_model_name, base_f1_score


def tunning_svc_model_metadata(df_train, df_test, threshold: float = 0.5):
    # Create a pipeline
    pipeline = SVC(class_weight="balanced")

    # Define the grid of hyperparameters to search
    parameter_grid = {
        "clf__C": [0.1, 1, 10],
        "clf__kernel": ["linear", "rbf"],
    }

    X_train, y_train = (
        df_train.drop(["Tweet", "clean_text", "Target"], axis=1),
        df_train["Target"],
    )
    X_test, y_test = (
        df_test.drop(["Tweet", "clean_text", "Target"], axis=1),
        df_test["Target"],
    )

    # Set up GridSearchCV
    grid_search = GridSearchCV(pipeline, parameter_grid, scoring="f1_macro", n_jobs=-1)

    # Fit the model
    grid_search.fit(X_train, y_train)

    # Best parameters
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameter_grid.keys()):
        print(f"\t{param_name}: {best_parameters[param_name]}")

    # Evaluate on test set
    y_proba = grid_search.predict_proba(X_test)
    y_pred = (y_proba[:, 1] >= threshold).astype(int)

    print_metrics(y_pred, y_test, "Best SVC - MD")

    return grid_search
