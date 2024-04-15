from django.conf import settings
from django.core.management import BaseCommand, get_commands

from kafka import KafkaProducer, KafkaConsumer
class Command(BaseCommand):
    # def add_arguments(self, *args, parser):
    #     parser.add_argument('-n', '--new', action='store', help='just', default=None)

    def add_arguments(self, parser, *args):
        parser.add_argument('-n', '--new', action='store', help='just', default=None)
        parser.add_argument('-a', '--a', action='store', help='jaust', default=None, dest='a')
        parser.add_argument('-b', '--b', action='store', help='just', default=None, dest='b')

    def handle(self, *args, **options):
        print(options.get('new'))
        # print(type(options['new']))
        print(args)
        import pdb
        a = options.get('a')
        b = options.get('b')
        pdb.set_trace()
        self.process(a, b)

    # def execute(self, *args, **options):
    #     print('pp')
    def process(self, a, b):
        res = a/b

        # Create a Kafka consumer in your Django view
        def my_kafka_consumer(request):
            # Create a KafkaConsumer object
            consumer = KafkaConsumer(settings.KAFKA_TOPIC_PREFIX + 'my-topic',
                                     bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                                     group_id=settings.KAFKA_CONSUMER_GROUP)
            # Loop over the messages in the Kafka topic
            for message in consumer:
                # Process the message
                print(message)
                process_message(message)
            # Return a HTTP response
            return HttpResponse(200)
        return res


# Define a function to process the messages received by the consumer
def process_message(message: str) -> None:
    print(f"message -- {message}")



