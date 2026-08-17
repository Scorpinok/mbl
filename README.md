# Real Estate Price Prediction — ML + Flask + Docker

![Model](https://img.shields.io/badge/Model-CatBoost-yellow?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-scikit--learn-orange?style=for-the-badge)
![Deploy](https://img.shields.io/badge/Deploy-Flask%20%2B%20Docker-blue?style=for-the-badge)

**Предсказание цены жилья на данных Sberbank Russian Housing Market (Kaggle): полный цикл от сырых данных до контейнеризованного сервиса.**

---

## Суть проекта

Датасет содержит 30 471 объект недвижимости и 292 "сырых", зашумлённых признака (числовые и категориальные, с заметной долей пропусков и выбросов). В проекте реализован полный ML-пайплайн — от очистки данных до обученной модели, обёрнутой во Flask-приложение и Docker-контейнер.

## Технологический стек

- **Модель:** CatBoostRegressor
- **Пайплайн:** scikit-learn (`Pipeline`, `ColumnTransformer`)
- **Деплой:** Flask, Docker

## Основные этапы работы

1. **Собственные трансформеры данных:** написаны кастомные классы `empty_drop` (удаление колонок с >20% пропусков) и `outlier_replace` (обработка выбросов) на базе `BaseEstimator`/`TransformerMixin`.
2. **Кодирование и снижение размерности:** категориальные признаки — `CatBoostEncoder`; численные — `StandardScaler` + `PCA` (сохранение 98% дисперсии).
3. **Подбор гиперпараметров:** `GridSearchCV` с 10-фолд кросс-валидацией по глубине дерева, learning rate и l2-регуляризации CatBoost.
4. **Деплой:** обученный пайплайн сериализован и обёрнут в Flask-приложение, упакованное в Docker-образ.

## Результаты

- **R² на тестовой выборке: 0.656**
- **RMSLE (официальная метрика соревнования): 0.231** — подбор гиперпараметров через GridSearchCV снизил RMSLE с 0.272 до 0.231 (~15% относительного улучшения); R² при этом почти не изменился, что ожидаемо — RMSLE как метрика соревнования сильнее чувствительна к относительной, а не абсолютной ошибке

## Как запустить

```bash
git clone https://github.com/Scorpinok/mbl.git
cd mbl
docker build -t my_flask_app:latest my_flask_app/
docker run -d -p 5000:5000 -v "<путь к директории с test.csv>:/app" my_flask_app:latest
```

Открыть **localhost:5000**, загрузить `test.csv` → получить `_predictions.csv` с предсказаниями.

---

*Проект выполнен в рамках итоговой работы курса «Машинное обучение» от GeekBrains*
