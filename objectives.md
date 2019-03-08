https://scikit-learn.org/stable/datasets/index.html#breast-cancer-wisconsin-diagnostic-dataset

- [x] get all feature drawer done
- [ ] record feature relationships
    * mean radius *higher radius -> strong malignant*
    * worst radius *higher radius -> strong malignant*

    * mean texture *higher texture -> weak malignant*
    * worst texture *higher texture -> medium malignant*

    * mean perimeter *higher perimeter -> high malignant*
    * worst perimeter *higher perimeter -> high malignant*

    * mean_area *higher area -> medium malignant*
    * worst_area *higher area -> high malignant*

    * mean_smoothness *higher smootherness -> weak malignant*
    * worst_smoothness *higher smootherness -> weak malignant*

    * mean_compactness *higher compactness -> medium malignant*
    * worst_compactness *higher compactness -> medium malignant*

    * mean_concavity *higher concavity -> medium malignant*
    * worst_concavity *higher concavity -> medium malignant*

    * mean_concave points *higher concave points -> strong malignant*
    * worst_concave points *higher concave points -> strong malignant*

    * mean_symmetry *higher symmetry -> weak malignant*
    * worst_symmetry *higher symmetry -> weak malignant*

    * mean_fractual dimension *higher symmetry -> uncorrelated*
    * worst_fractual dimension *higher symmetry -> weak malignant*

- [x] extract new features? *No, for now*

- [ ] select features
    **SELECTED**
        * worst radius
            *higher radius -> strong malignant*
            *tight left, spreads right*
        * worst perimeter
            *higher perimeter -> high malignant*
            *tight left, spreads right*
        * worst_area
            *higher area -> high malignant*
            *tight left, spreads right*
        * worst_concave points
            *higher concave points -> strong malignant*
            *little tight left, little spreads right*

    **RUNNER UPS**
        * mean radius *higher radius -> strong malignant*
        * mean perimeter *higher perimeter -> high malignant*
        * mean_area *higher area -> medium malignant*
        * mean_concave points *higher concave points -> strong malignant*


- [ ] normalize features
    * figure out which data is rougly normal
    * Try standard scaler and robust scaler
- [ ] split data into train and test
- [ ] build three classifiers


