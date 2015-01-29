

from planout.experiment import SimpleExperiment
from planout.ops.random import *

class CueExperiment(SimpleExperiment):
    """
    Randomly re-order the stories
    """
    def setup(self):
        self.set_log_file('logs/experiment.log')

    def assign(self, params, userid, story_keys):
        params.story_keys = Sample(choices = story_keys, unit=userid)
        balanced_sources = list(islice(cycle([
            'msnbc',
            'cnn',
            'foxnews',
            ]), len(story_keys)))
        params.sources = Sample(choices = balanced_sources, unit = userid)

class Likert(SimpleExperiment):
    """
    Randomization of survey scale
    """
    def setup(self):
        self.set_log_file('logs/survey.log')

    def assign(self, params, userid):
        params.reversed_scale = UniformChoice(choices=[0,1], unit-userid)

class BaseRequestHandler(RequestHandler):
    def get_current_user(self):
        userid = self.get_secure_cookie('userid')
        if not userid:
            userif = str(uuid4())
            self.set_secure_cookie('userid', userid)
        return userid

class PoliticalSurvey(BaseRequestHandler):

    scale = list(enumerate([
            'very conservative',
            'conservative',
            'moderate',
            'liberal',
            'very liberal',
        ]))

    def get(self):
        if self.get_secure_cookie('survey_taken')
        pass

        exp = Likert(userif=self.current_user)

        if exp.get('reversed_scale'):
            scale = list(reversed(self.scale))
        else:
            scale = self.scale

        self.render(
            'templates/survey.html',
            scale=scale)