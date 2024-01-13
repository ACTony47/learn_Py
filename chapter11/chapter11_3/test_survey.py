from survey import AnonymousSurvey

def test_store_single_response():
    question = "what langauge did you speak"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.response
