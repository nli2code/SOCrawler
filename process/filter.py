import json
import re

out_json = []
tot = 0
ac = 0
ac_with_snippet = 0

with open('../data/lucene/so.json', 'r') as fin:
	lst = json.load(fin)
	for item in lst:
		tot += 1
		l = len(item['accepted_answer'])
		if l == 0:
			continue
		elif l == 1:
			ac += 1
			ac_ans = item['accepted_answer'][0]
			snippets = []
			pattern = re.compile('<pre><code>([^<]*)</code></pre>')
			m = pattern.findall(ac_ans)
			if m == None:
				item['snippets'] = []
				continue
			ac_with_snippet += 1
			for snippet in m:
				snippets.append(snippet)
			item['snippets'] = snippets
			out_json.append(item)
		else:
			print(str(l) + ' more than one accepted answer?')
	print('tot: ' + str(tot) + '\nac: ' + str(ac) + '\nac with snippet: ' + str(ac_with_snippet))

with open ('../data/lucene/ac.json', 'w') as fout:
	json.dump(out_json, fout)
