tags = """
#mindset #curious_programmer #coder #hacking #artificialintelligence #webdeveloper #developer #codinglife #programmerrepublic #js #html #100daysofcode #predictiveprogramming #programmers #programming #datascience #devgirls #python3 #datascientist #webdesign #programmerhumor #stemgirls #java #artificialintelligenc #worklifebalance #cybersecurity #python #girlswhocode #coderlife #linux #css #100daysofdata #coders #womeninstem #javascript #codingpics #pythonprogramming #programmingjokes #stemeducation #codingdays #softwareengineering #programing #codingmemes #machinelearning #coderslife #coding #codingbootcamp #codergirl #motivation #programmer #computerscience #php #codingisfun #lifestyle #balance #softwaredeveloper #dataanalytics #workhardanywhere #programmersday #mindfulness #programminghumor #deeplearning #balancedlife #pythonhub #programmerlife #programmerslife #code #neuralnetworks #womenintech #programmingisfun #technology #informationtechnology #softwareengineer #programmerjokes #programmering #programacion #peoplewhocode #programmingmemes #pythoncode #development #coderpower #codingforkids #creativecoding #programminglife #pythonprojects #computerprogramming #webdevelopment #tech #software
"""

class Tag_Generator(object):
    def __init__(self, tag_list):
        self.tag_list = tag_list

    def sort_function(self):
        sorted_list = []
        _split = self.tag_list.split("#")
        
        for item in _split:
            item = item.strip("\n").strip()
            if item not in sorted_list:
                sorted_list.append(item)
        sorted_list = sorted(sorted_list)
        return sorted_list


    def tag_generator(self):
        sorted_list = self.sort_function()
        generated_tags = []
        while len(generated_tags) < 30:
            tag = random.choice(sorted_list)
            tag = "#" + tag
            if tag not in generated_tags:
                generated_tags.append(tag)
        return generated_tags


    def __repr__(self):
        tags = self.tag_generator()
        list = ""
        for element in tags:
            list += f"{element} "
        return list


if __name__ == "__main__":
    import random

    tag = Tag_Generator(tags)
    print(tag)

    print(f"\nTotal tags: {len(tag.tag_list)}")
    print(f"Unique tags: {len(tag.sort_function())}")
    
