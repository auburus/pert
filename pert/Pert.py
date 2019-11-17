
class Task:
	def __init__(self, id, title=None, description='', dependencies=[]):
		self.id = id
		self.title = title if title else id
		self.description = description

		if not all(map(lambda x: type(x) is Task, dependencies)):
			raise AttributeError("Invalid dependencies provided. "
					"Dependencies must be of type Task")

		self.dependencies = dependencies
