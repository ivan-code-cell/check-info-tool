def get_flow_content(line_list):
    flow_info = {'Opcode':line_list[6], 'Parameter':line_list[7].upper(), 'TestNumber':line_list[9], 'HardBin':line_list[16], 'SoftBin':line_list[18]}
    return flow_info


class ParseFlowTable:

    def read_flow_table(self, flow_path):

        with open(flow_path, 'r') as flow_file:
            for line_index, flow_table_line in enumerate(flow_file):
                if line_index > 3:
                    line_list = flow_table_line.split('\t')
                    if line_list[6] == '':
                        break
                    elif line_list[6] == 'Test' and line_list[5] != 'x':
                        self.__test_suite_list.append(get_flow_content(line_list))
                    else:
                        pass
                else:
                    pass

    def get_test_suite_info(self):
        return self.__test_suite_list

    def __init__(self):
        self.__test_suite_list = []

