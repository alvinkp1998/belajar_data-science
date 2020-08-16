# filtering recommendation
def filter_recommendation(df, genres=None, min_duration=None, max_duration=None, min_year=None, max_year=None, topN=10):
    data = df.copy()
    
    # initial filter
    if min_duration is not None:
        data = data.query('runtime >= @min_duration')
    if max_duration is not None:
        data = data.query('runtime <= @max_duration')
    if min_year is not None:
        data = data.query('release_year >= @min_year')
    if max_year is not None:
        data = data.query('release_year <= @max_year')
    if genres is not None:
        for genre in genres:
            data = data[data[genre] == 1]
    
    # weighting
    m = data['vote_count'].median()
    C = (data['vote_average'] * data['vote_count']).sum() / data['vote_count'].sum()
    data = data[(data['vote_count'] >= m)]
    
    def weighted_rating(df): 
        v = df['vote_count']
        R = df['vote_average']
        return (R*v + C*m) / (v+m)
    data["score"] = data.apply(weighted_rating, axis=1)
    
    # show only several columns
    result = data[["title", "genres", "release_year", "runtime", "vote_average", "vote_count", "score", "overview"]]
    return result.sort_values("score", ascending=False).head(topN)