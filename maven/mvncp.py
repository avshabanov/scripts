import argparse
from os import listdir
from os.path import isfile, join
from os.path import expanduser

parser = argparse.ArgumentParser(description = 'Copies maven artifact from local maven repository to the mirror repo')


parser.add_argument('-g', '--groupId', help = 'Artifact Group ID, e.g. org.springframework', dest = "group_id", required = True)
parser.add_argument('-v', '--version', help = 'Artifact Version, e.g. 3.1.1', required = True)
parser.add_argument('-a', '--artifactId', help = 'Artifact ID, e.g. spring-core', dest = "artifact_id", required = True)
parser.add_argument('-t', '--target', help = 'Target maven directory', required = True)

args = parser.parse_args()
print 'Args: g={group_id}, v={version}, a={artifact_id}, target={target}'.format(group_id = args.group_id,
    version = args.version, artifact_id = args.artifact_id, target = args.target)

home_folder = expanduser("~")
artifact_dir = home_folder + '/.m2/repository/' + args.group_id.replace('.', '/') + '/' + args.artifact_id + '/' + args.version;

onlyfiles = [ f for f in listdir(artifact_dir) if isfile(join(artifact_dir, f)) ]
for f in onlyfiles:
    print 'f = {}'.format(f)

print 'd = {}'.format(artifact_dir)

