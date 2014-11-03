import tag
import repeat
from text import TextBlock
from parser import BlockSequence
from iteration import IterationBlock

def token_class():
	return SumTagToken


class SumTagToken(repeat.AbstractRepeatTagToken):

	def parse(self, context):
	
		(counters, content) = repeat.AbstractRepeatTagToken.parse(self, context)
		
		#  we put this here since we still need to process the inner content up to @end even for an empty range!
		if len(counters) == 0:
			return
		
		block = BlockSequence([TextBlock('('), content, TextBlock(')')])
		for counter in reversed(counters):
			block = IterationBlock(counter, block, before = '(', between = ' + ', after = ')')
		
		context.append_block(block)
