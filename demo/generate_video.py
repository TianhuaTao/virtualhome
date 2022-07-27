from virtualhome.simulation.unity_simulator.comm_unity import UnityCommunication


def main():
    script = ['<char0> [Walk] <tv> (1)', '<char0> [switchon] <tv> (1)', '<char0> [Walk] <sofa> (1)',
              '<char0> [Sit] <sofa> (1)', '<char0> [Watch] <tv> (1)']  # Add here your script

    print('Starting Unity...')
    comm = UnityCommunication(file_name='../simulator/linux_exec.v2.3.0.x86_64')

    print('Starting scene...')
    comm.reset()
    comm.add_character('Chars/Female1')

    print('Generating script...')
    comm.render_script(script, recording=True, find_solution=True)

    s, graph = comm.environment_graph()

    print(graph)

if __name__ == '__main__':
    main()
