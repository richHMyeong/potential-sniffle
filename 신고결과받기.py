def solution(id_list, report, k):
    answer = [0 for x in range(len(id_list))]
    
    id_dict = {}
    for cnt, id in enumerate(id_list):
        id_dict[id] = cnt

    singo = [[] for x in range(len(id_list))]  # 나를 신고한 사람들
    singo_cnt = [0 for x in range(len(id_list))]  # 내가 신고당한 횟수

    for x in report:
        a, b = x.split(' ')

        if a not in singo[id_dict[b]]:
            singo[id_dict[b]].append(a)  # ex) id_dict['frodo']는 1. singo[1]은 frodo의 리스트. frodo를 신고한 사람들을 singo에 추가.
            singo_cnt[id_dict[b]] += 1  # 신고당한 횟수 1 더해주기

        # 만약  singo_cnt가 k가 되면
    for num, cnt in enumerate(singo_cnt):
        if cnt>=k:
            for id in singo[num]:
                answer[id_dict[id]] += 1

    return answer
