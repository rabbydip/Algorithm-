# Import the OBO parser from GOATools
from goatools import obo_parser
import wget
import os
go_obo_url = 'http://purl.obolibrary.org/obo/go/go-basic.obo'
data_folder = os.getcwd() + '/data'

# Check if we have the ./data directory already
if(not os.path.isfile(data_folder)):
    # Emulate mkdir -p (no error if folder exists)
    try:
        os.mkdir(data_folder)
    except OSError as e:
        if(e.errno != 17):
            raise e
else:
    raise Exception('Data path (' + data_folder + ') exists as a file. '
                   'Please rename, remove or change the desired location of the data path.')

# Check if the file exists already
if(not os.path.isfile(data_folder+'/go-basic.obo')):
    go_obo = wget.download(go_obo_url, data_folder+'/go-basic.obo')
else:
    go_obo = data_folder+'/go-basic.obo'
print(go_obo)
go = obo_parser.GODag(go_obo)
go_id = 'GO:0048527'
go_term = go[go_id]
print(go_term)
print('GO term name: {}'.format(go_term.name))
print('GO term namespace: {}'.format(go_term.namespace))
for term in go_term.parents:
    print(term)
for term in go_term.children:
    print(term)


def transitive_closure(go_term, go):
    go_term_set = set()
    find_parents(go_term, go, go_term_set)
    find_children(go_term, go, go_term_set)
    return go_term_set


def find_parents(term1, go, go_term_set={}, ret=False):
    for term2 in term1.parents:
        go_term_set.update({term2})

        # Recurse on term to find all parents
        find_parents(term2, go, go_term_set)
    if (ret):
        return go_term_set


def find_children(term1, go, go_term_set={}, ret=False):
    for term2 in term1.children:
        go_term_set.update({term2})

        # Recurse on term to find all children
        find_children(term2, go, go_term_set)
    if (ret):
        return go_term_set
go_term_set = transitive_closure(go_term, go)
for term in go_term_set:
    print(term)
rec = go[go_id]
parents = rec.get_all_parents()
children = rec.get_all_children()
for term in parents.union(children):
    print(go[term])
growth_count = 0
for go_term in go.values():
    if 'growth' in go_term.name:
        growth_count += 1

print('Number of GO terms with "growth" in their name: {}'.format(growth_count))


def common_parent_go_ids(terms, go):
    '''
        This function finds the common ancestors in the GO
        tree of the list of terms in the input.
    '''
    # Find candidates from first
    rec = go[terms[0]]
    candidates = rec.get_all_parents()
    candidates.update({terms[0]})

    # Find intersection with second to nth term
    for term in terms[1:]:
        rec = go[term]
        parents = rec.get_all_parents()
        parents.update({term})

        # Find the intersection with the candidates, and update.
        candidates.intersection_update(parents)

    return candidates
def deepest_common_ancestor(terms, go):
    '''
        This function gets the nearest common ancestor
        using the above function.
        Only returns single most specific - assumes unique exists.
    '''
    # Take the element at maximum depth.
    return max(common_parent_go_ids(terms, go), key=lambda t: go[t].depth)
go_id1 = 'GO:0097178'
go_id_id1_dca = deepest_common_ancestor([go_id, go_id1], go)
print('The nearest common ancestor of\n\t{} ({})\nand\n\t{} ({})\nis\n\t{} ({})'
      .format(go_id, go[go_id].name,
              go_id1, go[go_id1].name,
              go_id_id1_dca, go[go_id_id1_dca].name))
go_id2 = 'GO:0097192'
rec = go[go_id2]
lineage_png = go_id2 + '-lineage.png'
go.draw_lineage([rec], lineage_img=lineage_png)
from IPython.display import Image
Image(lineage_png)
